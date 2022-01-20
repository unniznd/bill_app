import 'package:flutter/material.dart';
import '../backend/auth.dart';
import 'layout.dart';
import 'package:encrypt/encrypt.dart' as encrypt;
import 'dart:convert';

class LoginScreen extends StatefulWidget {
  @override
  _LoginScreenState createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  TextEditingController username = new TextEditingController();
  TextEditingController password = new TextEditingController();

  void _showToast(BuildContext context, String txt) {
    final scaffold = ScaffoldMessenger.of(context);
    scaffold.showSnackBar(
      SnackBar(
        content: Text(txt),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    double width = MediaQuery.of(context).size.width;
    double height = MediaQuery.of(context).size.height;

    return Scaffold(
      body: SafeArea(
          child: SingleChildScrollView(
        child: Container(
          margin: EdgeInsets.all(10),
          child: Column(
            children: [
              SizedBox(
                height: height * 0.4,
              ),
              TextField(
                controller: username,
                decoration: InputDecoration(
                  border: OutlineInputBorder(),
                  hintText: 'Username',
                  label: Text('Username'),
                ),
              ),
              SizedBox(
                height: height * 0.04,
              ),
              TextField(
                controller: password,
                obscureText: true,
                enableSuggestions: false,
                autocorrect: false,
                decoration: InputDecoration(
                  border: OutlineInputBorder(),
                  hintText: 'Password',
                  label: Text('Password'),
                ),
              ),
              SizedBox(
                height: height * 0.04,
              ),
              Container(
                height: 50,
                width: double.infinity,
                child: ElevatedButton(
                  onPressed: () async {
                    if (username.text != '' && password.text != '') {
                      final key = encrypt.Key.fromBase64(
                          'IkB0Lq7xZHzfSLgVnvDjBm8mXe6jQclfMUyfaoAUK4E=');

                      final fernet = encrypt.Fernet(key);
                      final encrypter = encrypt.Encrypter(fernet);

                      final txt = encrypter.encrypt(password.text);
                      if (await authenticate(username.text, txt.base64)) {
                        Navigator.of(context).pushReplacement(
                          MaterialPageRoute(
                            builder: (context) => LayoutScreen(),
                          ),
                        );
                      } else {
                        _showToast(context, "Invalid Credintials");
                      }
                    } else {
                      _showToast(context, 'Empty username or password');
                    }
                  },
                  style: ButtonStyle(
                    backgroundColor: MaterialStateProperty.all(Colors.purple),
                  ),
                  child: Text(
                    "Login",
                    style: TextStyle(
                      color: Colors.white,
                      fontSize: 20,
                    ),
                  ),
                ),
              )
            ],
          ),
        ),
      )),
    );
  }
}
