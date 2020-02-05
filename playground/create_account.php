
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


<h1>Crie sua conta aqui</h1>

<form method="POST" action="create.php">
  Username:<br>
  <input type="text" name="user"><br>
  Password:<br>
  <input type="text" name="password"><br><br>
  email:<br>
  <input type="text" name="email"><br><br>
  <input type="submit" value="Submit">
</form>

</body>
</html>