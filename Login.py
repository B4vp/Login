<!-- Made By p3l0r -->

<!DOCTYPE html>

<html>

<head>

<meta charset="utf-8">

<title>Login Form</title>

<link rel='stylesheet' href='https://use.fontawesome.com/releases/v5.5.0/css/all.css' integrity='sha384-B4dIYHKNBt8Bc12p+WXckhzcICo0wtJAoU8YZTY5qE0Id1GSseTk6S+L3BlXeVIU' crossorigin='anonymous'>

</head>

<body>

    <header>

        

    </header><br><br>

    

    <main id="form">

    <section style="display: inline;" id="ma">

    <i class='far fa-user-circle' style='font-size:84px;padding: 5px; color: #27a5df'></i>

        <h1> Login </h1><hr><br>

        

        Username

        <input id="un" placeholder="Enter username..." type="text" /><br><br>

        

        Password

        <input type="password" id="psw" placeholder="Enter password..." /><br><br>

        

       <i class="far fa-check-circle" style="font-size: 20px;color: #27a5df" onclick="uc()" id="1"></i>

           

       <i class="far fa-circle" style="font-size: 20px;display: none;color: #27a5df" onclick="ch()" id="2"></i> Remember Me<br><br>

        

        <button onclick="login()">Login

        <i class="fas fa-sign-in-alt"></i>

        </button>

    </section>

    

    <section id="out" style="display: none;">

        <i class='far fa-user-circle' style='font-size:84px;padding: 5px; color: #27a5df'></i>

        <h1> User Info </h1><hr>

        <p id="info"></p><br />

        <button onclick="logout()">Logout

       <i class="fas fa-power-off"></i>

        </button>

    </section>

    </main>

    

    <br><br>

    

    <footer id="footer">

        Made BY <a href="https://www.sololearn.com/Profile/6426776/?ref=app"> VEDANG </a>

        

    </footer><br /><br /><br />

</body>

</html>

