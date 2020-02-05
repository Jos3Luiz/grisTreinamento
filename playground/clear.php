<!DOCTYPE html>
<html>

 <head>
 
  <title>limpar </title>
  
  <?php
  include_once  'connect_db.php';
  include_once  'header.php';
  ?>


 </head>

<body>

<?php

			$sql="DELETE FROM posts WHERE 1;";
			$result= mysqli_query($conn,$sql);
			

?>
<meta http-equiv="refresh" content="0; URL='home.php'"/>
</body>
</html>