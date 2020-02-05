
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

<?php

//connects to db
	$username=$_POST['user'];
	$password=$_POST['password'];
	$email=$_POST['email'];

	$sql="select * from users WHERE username='$username';";
	$result= mysqli_query($conn,$sql);
	if (mysqli_num_rows($result) === 0)
	{
		$sql="insert into users (username,password,email) VALUES ('$username','$password','$email');";
		
		$result= mysqli_query($conn,$sql);
		setcookie('CookieUsername',$username,time()+60*60*7);
		setcookie('CookiePassword',$password,time()+60*60*7);
		session_start();
		$_SESSION['username'] =$username;
		echo "login criado com sucesso<br>";
		echo "<a href='home.php'>clique aqui</a> para prosseguir para a sala de chat";
	}
	else{
		echo "já existe um usuario com esse nome!";
		echo "<br><a href='create_account.php'>clique aqui</a> para voltar";
	}

?>
</body>
</html>
