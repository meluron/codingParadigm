<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
	</head>
	<body>
		<h1>28/01/2025 | Coding Guidelines</h1>
		<h2>Coding</h2>
		<ul>
			<li>Do not over comment your code, comment <b>why</b> not what.</li>
			<li>Keep README.md uptodate.</li>
			<li>I prefer component-based programming which means that every function should have some common accessories that can be used to perform different tasks around a function, this is what i call class-based functional programming, see below.</li>
			<li>I prefer test-driven coding, after creating the function template, set up all the accessories. Write tests even before start implementing the logic to stay on track.</li>
			<li>Follow camelCase across language to be consistent.</li>
		</ul>
		<h2>Class-based functional programming</h2>
		<p>All major functions are classes inheriting FBC. For distinguishing between actual classes and class-based functions, I use camelCase naming convention for class-based functions and PascalCase for actual class. All class-based functions have the following accessories:</p>
		<ul>
			<li>obj.<b>info()</b>: prints details about the current state of the function</li>
			<li>obj.<b>test()</b>: runs a test on the function if anything broke while making any changes</li>
			<li>obj.<b>plot()</b>: shows anything graphics related (plots, images, ...) if applicable</li>
			<li>obj.<b>save()</b>: to save output</li>
			<li>obj.<b>run()</b>: to run the function, contains the actual implementation of the function</li>
		</ul>
		<a href="./functionTemplate.py">Template</a><span> | </span><a href="./FBC.py">FBC</a><br>
	</body>
</html>