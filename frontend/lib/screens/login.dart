import 'package:flutter/material.dart';
import '../backend/auth.dart';
import './home.dart';

class LoginScreen extends StatefulWidget {
  const LoginScreen({Key? key}) : super(key: key);

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
                      if (await authenticate(username.text, password.text)) {
                        Navigator.of(context).pushReplacement(
                          MaterialPageRoute(
                            builder: (context) => HomeScreen(),
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
