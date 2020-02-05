<?php
 $_SESSION['username']="";
 $_SESSION['password']="";
 unset($_SESSION['username']);
 unset($_SESSION['password']);
 
 session_destroy();
 echo"<script> window.location.href = '../index.php' ; </script>";
 exit();
 ?>
