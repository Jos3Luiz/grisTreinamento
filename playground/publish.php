
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
	session_start();

	if (isset($_POST['titulo'] , $_POST['conteudo'],$_SESSION['username'] ))
	{
		$username=$_SESSION['username']; 
		$titulo=$_POST['titulo']; 
		$conteudo=$_POST['conteudo']; 

		if ($titulo=="" or $conteudo=="" or $username=="" )
		{
			echo "campos nulos nao sao permitidos";
		}
		else
		{
			$agora=time();
			$likes=0;
			$sql="insert into posts (poster,titulo,conteudo,date,likes) VALUES ('$username','$titulo','$conteudo','$agora','$likes');";
			$result= mysqli_query($conn,$sql);
			if ($result===False)
        		{
                		echo "<br>Error running query: " . mysqli_error($conn)."<br>";
        		}

			echo "Postado com sucesso";

	

		}
	}




?>
<meta http-equiv="refresh" content="1; URL='home.php'"/>
</body>
</html>
