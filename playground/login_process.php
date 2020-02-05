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
	$username=$_POST['username'];
	$password=$_POST['password'];
	

	$sql="select * from users WHERE username='$username' AND password='$password';";
	echo $sql;
	$result= mysqli_query($conn,$sql);
	if ($result===False)
	{
		echo "<br>usuario inexistente<br>";
		echo "<br>Error running query: " . mysqli_error($conn)."<br>";
	}
	else 
	{
			
		$row=mysqli_fetch_assoc($result);
		$password_bd= $row['password'];
		if ($password_bd!=null)
		{
			setcookie('CookieUsername',$username,time()+60*60*7);
			setcookie('CookiePassword',$password,time()+60*60*7);
			echo "<br>sua senha eh ".$password_bd;
			session_start();
			$_SESSION['username'] =$username;
			echo "<br><a href=\"/home.php\">acessar</a>";
		}
		else{
			echo "<br>senha incorreta";
		}

		    
		    
	}

?>
</body>
</html>
