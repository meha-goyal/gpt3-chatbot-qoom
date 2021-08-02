# Build an AI Chatbot (Editing in Progress)

## Introduction

## Goals:
1. Create an **AI Chatbot** that responds to user questions.
2. Build a page that displays the **chatbot popup** window

## Technologies you will Learn:
1. Submitting data and recieving generated responses using the `OPENAI` API
2. Using `JavaScript` functions and `Flask` to send and recieve data from the page to the API
3. The `HTML/CSS` necessary to create a popup chatbot page.

## Strategy
> 1. <a href="#">Create a basic input and output on chatbot page</a>
> 2. <a href="#">Access API using Python</a> 
> 3. <a href="#">Train AI model on user data</a> 
> 4. <a href="#">Connect API functionality to the chatbot page</a> 
> 5. <a href="#">Design chatbot popup page</a>

## Need Help?

Get help from the Qoom team and our community members. <a href="https://discord.gg/G4cFUdTq2H" target="_blank">Join Qoom Community</a>

---

<h2 id="landing">1. Create basic page to display input and output</h2>

It is hard to build the chatbot and test its functionality without starting with a basic page for sending inputs and recieving outputs.

Let's now implement this design using the following strategy:
1. Define the structure of the design using `HTML`
2. Make it look like what we want using `CSS`

If you haven't already, create an account on <a href="https://www.qoom.io" target="_blank">https://www.qoom.io</a> and follow along. We are using `Qoom` so that we can create a login system without writing any backend code. After creating an account, create a `New Project` and name it with a fake company name of your choosing. Then add the following `html` elements to the `<body>` elements:

```html
<body>
	
	<div class="chat-input">      
        <input type="text" name="question" placeholder="How can we help you?"/>
      <button type="submit" onclick='send()'>Submit</button>
    </div>
    
    <div id="textarea" readonly class="chat-logs">
     </div>

</body>

```
The first div holds an input element, and a button. The input has the placeholder "How can we help you?" in order to prompt the user to ask a question. The button, with type submit and the corressponding function send, will send the user's request to the back end later on.

The second div with id="textarea" is where the output will be printed.


---


<h2 id="signup">2. Use API to begin chatbot</h2>

Most of the following work will be done in one python file (app.py). 

So create a new page called `signup.html` and replace the `<head>` element with that that is inside of `index.html`:

Here is the `html` template we will use for all the remaining pages:
```html
<!DOCTYPE html>
<html>

	<head>
		<meta name="viewport" content="width=device-width, initial-scale=0.5">
		<link rel="stylesheet" href="styles.css">
		<script type="module" src="script.js"></script>
		<link rel="shortcut icon" type="image/jpg" href="pug.png"/>
		<title>Sign Up!</title>
	</head>

	<body>
		<nav>

		</nav>
		<main>
			<div></div>
		</main>
		<footer>
			© 2021 The Doggo Group
		</footer>
	</body>

</html>

```

Now in our signup page we want to just allow the user to login or go back to home.

```html
<nav>
	<a href='index'>Home</a>
	<a href='login'>Login</a>
</nav>
```

Finally we can create our signup form like so:

```html
<main>
	<div>
		<h2>Sign Up</h2>
		<form action='/~/Doggo/signup' method='POST' enctype='multipart/form-data'>
			<input type='email' name='username' placeholder='Email' required>
			<input type='password' name='password' placeholder='Password' required>
			<label>Your Avatar</label>
			<input type='file' assets='image/*' name='avatar' required>
			<input type='submit' value='Sign up'>
			
			<!-- THIS TELLS OUR SERVER WHERE TO SEND THE USER AFTER GETTING THE DATA-->
			<input type='hidden' name='redirecturl' value='/~/Doggo/account'>
		</form>	
	</div>
</main>
```
The form element has the following powers:
> 1. **action='/~/Doggo/signup'**: This tells the browser to send the data to the `/~/Doggo/signup` function that is defined on the server
> 2. **method='POST'**: This tells the browser to send the data in a way that the browser can encrypt it. Thus keeping it secret from our ISP.
> 3. **enctype='multipart/form-data'**: This tells the browser what encoding to use to send the data. This encoding allows us to send images.


Finally we can add the css for our `form` element:

```css
main form {
	display:flex;
	flex-direction:column;
	gap:20px;
	margin-bottom:20px;
	width:320px;
}

main form input {
	width:100%;
	padding:0.5em;
	box-sizing:border-box;
	border-radius:3px;
	border:none;
}

main form input[type=submit]:hover {
	background-color:#dfdfdf;
	cursor:pointer;
}
```


Our page now looks like this:

![](assets/signup.png)

<a href="#top" class="back2top">Back To Top</a>

---

<h2 id="account">3. Create <code>account</code> page</h2>

In the account page we can do a lot, but for this tutorial we are going to just show the data the user entered when signing up.

Here is the `html`:

```html
<!DOCTYPE html>
<html>

	<head>
		<meta name="viewport" content="width=device-width, initial-scale=0.5">
		<link rel="stylesheet" href="styles.css">
		<script type="module" src="script.js"></script>
		<link rel="shortcut icon" type="image/jpg" href="pug.png"/>
		<title>Sign Up!</title>
	</head>

	<body>
		<nav>
			<a href='index'>Home</a>
			<a onclick='logout()'>Logout</a>
		</nav>
		<main>
			{{#private}}
			<div>
				<h2>Your Account</h2>
				<h3>{{username}}</h3>
				<img src='{{avatar}}'>
			</div>
			{{/private}}
			
			{{^private}}
				<script>
					location.href = 'index';
				</script>
			{{/private}}
		</main>
		<footer>
			© 2021 The Doggo Group
		</footer>
	</body>

</html>
```

We are using `Mustache` again to show the account data. We are also using Mustache with some simple `Javascript` to redirect the user to the home page if they are not logged in.

<a href="#top" class="back2top">Back To Top</a>

---

<h2 id="logout">4. Create <code>logout</code> feature</h2>

Now that we have signed the user in, we need to give them a way to log out. To do this, we just need to go to the `script.js` and create our `logout` function:

```js
window.logout = function() {

	// TELLS OUR SERVER TO LOG THE USER OUT
	fetch('/~/Doggo/logout', { method: 'POST'});
	
	// TELLS OUR BROWSER TO SHOW A MESSAGE TO OUR USER
	alert('Logged Out!');
	
	// REDIRECTS THE USER TO THE HOMEPAGE
	location.href = '/~/Doggo/index'
}
```
<a href="#top" class="back2top">Back To Top</a>

---

<h2 id="login">5. Create <code>login</code> page</h2>

The login page now is very similar to the `signup` page. We just need to send the data to a different action on the server like so:

```html
<!DOCTYPE html>
<html>

	<head>
		<meta name="viewport" content="width=device-width, initial-scale=0.5">
		<link rel="stylesheet" href="styles.css">
		<script type="module" src="script.js"></script>
		<link rel="shortcut icon" type="image/jpg" href="pug.png"/>
		<title>Login!</title>
	</head>

	<body>
		<nav>
			<a href='index'>Home</a>
			<a href='signup'>Signup</a>
		</nav>
		<main>
			<div>
				<h2>Login</h2>
				<form action='/~/Doggo/login' method='POST' enctype='multipart/form-data'>
					<input type='email' name='username' placeholder='Email' required>
					<input type='password' name='password' placeholder='Password' required>
				
					<input type='submit' value='Log In'>
					<input type='hidden' name='redirecturl' value='/~/Doggo/account'>
				</form>	
			</div>
		</main>
		<footer>
			© 2021 The Doggo Group
		</footer>
	</body>

</html>

```

Now we are done!

---

## Challenges:

> 1. Add profile pictures for both the user and qoombot!

> 2. Style the buttons differently on mobile. (Hint: Research `CSS media queries`)

> 3. Create a `preview of the profile image` the user uploaded so they can see it before hitting the sign up button. (This will require you to search the internet for a solution).
