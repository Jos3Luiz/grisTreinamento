
<!DOCTYPE html>
<html>

 <head>
 
  <title>Bem vindo ao meu chat</title>
  
  <?php
  include_once  'connect_db.php';
  include_once  'header.php';
  ?>


 </head>

<body>

<h1>Faça o login aqui</h1>

<form method="POST" action="login_process.php">
  Username:<br>
  <input type="text" name="username"><br>
  Password:<br>
  <input type="text" name="password"><br><br>
  <input type="submit" value="Submit">
</form>

<br>
Ou crie sua conta <a href="create_account.php">aqui</a>
<br>


</body>
</html>