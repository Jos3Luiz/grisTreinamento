
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
<form action="clear.php" method="get" id="form1">

<button type="submit" form="form1" value="Submit">Limpar o Chat</button>
</form>


 <a href="logoff.php">Logoff</a>

<br>


<?php
  session_start();
$user= $_SESSION['username']; 
if ($user=="")
{
  header('Location: index.php'); 
}
?>
 
<br> Bem vindo ao chat, <?php echo $user; ?>. Conversem entre si e sejam educados !</br>
<div class="boxed">
    


<form id="myForm" action="publish.php" method="post">
    usuario: <?php echo $user; ?> <br>
    Titulo: <input type="text" name="titulo" size="50" autofocus/><br>
    Mensagem: <input type="text" name="conteudo" size="100" /><br>
    <input type="submit" value="Submit" />
</form>


</div>
<br>



    <?php
    //daqui pra baixo ficou foda kkkkk

    $sql="SELECT * FROM posts ;";
    $result= mysqli_query($conn,$sql);
    
    while($row = mysqli_fetch_array($result))
    {
        echo "<div class=\"boxed\">";
        echo "Autor: ".$row['poster']."<br>";
        echo "Titulo:".$row['titulo']."<br><br>";
        echo "Postagem: ".$row['conteudo']."<br>";
        $date=$row['date'];
        echo "<br>Publicado em:".date('m/d/Y', $date)."<br>";
        echo "Likes: ".$row['likes']."<br>";
        


        echo "</div><br>";

    }




?>


</body>
</html>







