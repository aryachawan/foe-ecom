function Verification(){
  const form = document.getElementById('form');
  const username = document.getElementById('username');
  const email = document.getElementById('email');
  const password = document.getElementById('password');
  const password2 = document.getElementById('password2');
  if (username.value.length<=3)
  {
      username.style.borderColor = "red";
  }
  else
  {
    username.style.borderColor = "green";
  }
  var emailregex=/^[a-z0-9]+@[a-zA-Z]+\.[a-zA-Z]{2,3}$/
  var emailtest=emailregex.test(email.value)
  if(!emailtest)
  {
    email.style.borderColor = "red";
  }
  else
  {
    email.style.borderColor = "green";
  }
  if ((password.value.length != password2.value.length) || password.value.length<6)
  {
    password.style.borderColor = "red"
    password2.style.borderColor = "red"
    if (password.value.length<6)
    {
      alert("Passwords Too Short")
    }
    if (password.value.length != password2.value.length)
    {
      alert("Passwords Dont Match")
    }
  }
  else
  {
    password.style.borderColor = "green"
    password2.style.borderColor = "green"
  }
};
