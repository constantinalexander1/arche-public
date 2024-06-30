/*
	Taken from https://github.com/vrana/games
	Modified (2024)
*/

(function () {
	var board = document.getElementById('board');
	var maxX;
	var maxY;
	var step = 0;
	var speed = 20;
	var time;

	window.onresize = function () {
		maxX = board.clientWidth / 5;
		maxY = board.clientHeight / 5;
	};
	window.onresize();
	
	function createSnake(x, y, angle, keyLeft, keyRight, keyBoost, className) {
		return {
			x: x,
			y: y,
			angle: angle,
			speed: 1,
			keyLeft: keyLeft,
			keyRight: keyRight,
			keyBoost: keyBoost,
			className: className,
			points: createPoints(x, y, className),
			invincible: 0,
		};
	}
	
	function createPoints(x, y, className) {
		var points = [];
		var length = 30;
		for (var i = 0; i < length; i++) {
			points.push(createPoint(x - length + i + 1, y, 'point ' + className));
		}
		updateScore(className, points.length);
		return points;
	}
	
	function randomX() {
		return Math.floor(Math.random() * maxX);
	}
	
	function randomY() {
		return Math.floor(Math.random() * maxY);
	}
	
	var Keys = {
		LEFT: 37,
		RIGHT: 39,
		UP: 38,
		A: 65,
		B: 66,
		M: 77,
		N: 78,
		X: 88,
		Z: 90,
	};

	var snakes = [
		createSnake(40, 40, 0, Keys.LEFT, Keys.RIGHT, Keys.UP, ''),
		// createSnake(40, 60, 0, Keys.Z, Keys.X, Keys.A, 'snake2'),
	];
	
	var foods = [];
	for (var i = 0; i < 10; i++) {
		var value = Math.floor(Math.random() * (4 - 1 + 1) + 1)
		var className = "food" + value;
		var point = createPoint(randomX(), randomY(), className);
		foods.push(point);
	}

	function createPoint(x, y, className) {
		foodValue = parseInt(className.substr(4))
		if (!foodValue) {
			foodValue = 1;
		}

		var point = {
			point: document.createElement('div'),
			value: foodValue
		};

		point.point.className = className;

		putPoint(point, x, y);
		board.appendChild(point.point);
		return point;
	}
	
	var pressedKeys = {};
	
	document.body.onkeyup = function(event) {
		delete pressedKeys[event.keyCode];
	};
	
	document.body.onkeydown = function(event) {
		pressedKeys[event.keyCode] = true;
	}

	document.getElementById("pause-button").onclick = function() {
		if (paused) {
			paused = false;
		} else {
			paused = true;
		}
	};

	
	function changeAngle(snake, delta) {
		snake.angle = (snake.angle + 10 * delta + 360) % 360;
	}
	
	function collides(point, x, y, delta) {
		return Math.abs(x - getX(point)) < delta && Math.abs(y - getY(point)) < delta;
	}
	
	function putPoint(point, x, y) {
		point.x = x;
		point.y = y;
		point.point.style.marginLeft = 5 * x + 'px';
		point.point.style.marginTop = 5 * y + 'px';
	}
	
	function removePoint(point, x, y) {
		if (point.point.parentElement) {
			point.point.parentElement.removeChild(point.point);
		}
	}
	
	function getX(point) {
		return point.x;
	}
	
	function getY(point) {
		return point.y;
	}
	
	function die(snake) {
		for (var i = 0, point; point = snake.points[i]; i++) {
			if (i % 10 == 0) {
				point.fromDead = true;
				point.point.className = 'food2 fromDead';
				point.value = 1;
				foods.push(point);
			} else {
				removePoint(point);
			}
		}
		snake.x = randomX();
		snake.y = randomY();
		snake.angle = 0;
		snake.invincible = 10;
		snake.points = createPoints(snake.x, snake.y, snake.className);
	}
	
	function moveSnake(snake) {
		snake.speed = 1;
		for (var keyCode in pressedKeys) {
			if (keyCode == snake.keyLeft) {
				changeAngle(snake, -1);
			} else if (keyCode == snake.keyRight) {
				changeAngle(snake, 1);
			}
			if (keyCode == snake.keyBoost) {
				snake.speed = 2;
			}
		}
		snake.x = (snake.x + Math.cos(snake.angle / 180 * Math.PI) * snake.speed + maxX) % maxX;
		snake.y = (snake.y + Math.sin(snake.angle / 180 * Math.PI) * snake.speed + maxY) % maxY;
		if (snake.invincible) {
			snake.invincible--;
		}
		
		if (!snake.invincible) {
			for (var i = 0; i < snakes.length; i++) {
				if (snake != snakes[i] && !snakes[i].invincible) {
					for (var j = 0; j < snakes[i].points.length; j++) {
						if (collides(snakes[i].points[j], snake.x, snake.y, 3)) {
							die(snake);
							return;
						}
					}
				}
			}
		}
		
		if (snake.speed > 1 && snake.points.length > 1 && step % 10 == 0) {
			var food = snake.points.shift();
			food.fromDead = true;
			food.point.className = 'food2 fromDead';
			food.value = 1;
			foods.push(food);
		}
		
		// TODO: add more sizes
		var ate = 0;
		for (var i = 0; i < foods.length; i++) {
			var food = foods[i];

			if (!food) continue
			
			delta = 1;
			switch (food.value) {
				case 1: delta = 1
				case 2: delta = 2
				case 3: delta = 3
				case 4: delta = 4
			}

			if (food && collides(food, snake.x, snake.y, delta)) {
				if (!food.fromDead) {

					foodValue = food.value;
					if (!foodValue) foodValue = 1;
					putPoint(food, randomX(), randomY());
					ate += foodValue;
				} else {
					removePoint(food);
					foods[i] = undefined;
					ate++;
				}
			}
		}
		var point = snake.points.shift();
		if (!point) {
			return;
		}
		for (var i = 0; i < ate; i++) {
			snake.points.unshift(createPoint(getX(point), getY(point), 'point ' + snake.className));
		}
		putPoint(point, snake.x, snake.y);
		snake.points.push(point);
		updateScore(snake.className, snake.points.length);
	}
	
	function updateScore(className, score) {
		document.querySelector('.score' + (className ? '.' + className : '')).textContent = score;
	}
	
	var timeout;
	var paused = false;
	function loop() {
		for (var i = 0, snake; snake = snakes[i]; i++) {
			if (!paused) moveSnake(snake);
		}
		step++;
		var oldTime = time;
		time = Date.now();
		timeout = window.setTimeout(loop, 3000 / speed + oldTime - time);
	}
	
	window.onblur = function () {
		window.clearTimeout(timeout);
	};
	
	window.onfocus = function () {
		time = Date.now() - 1000 / speed;
		loop();
	};
	
	if (document.hasFocus()) {
		window.onfocus();
	}
})();
