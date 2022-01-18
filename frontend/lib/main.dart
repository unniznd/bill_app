import 'package:flutter/material.dart';
import 'package:frontend/screens/home.dart';
import './screens/login.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';
import 'backend/config.dart';
import 'package:http/http.dart' as http;

const storage = FlutterSecureStorage();

void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  runApp(
    BillingApp(),
  );
}

class BillingApp extends StatefulWidget {
  @override
  _BillingAppState createState() => _BillingAppState();
}

class _BillingAppState extends State<BillingApp> {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        scaffoldBackgroundColor: Colors.white,
      ),
      home: LoginScreen(),
      // home: FutureBuilder(
      //   future: storage.read(key: "token"),
      //   builder: (context, snapshot) {
      //     if (snapshot.connectionState == ConnectionState.done) {
      //       if (snapshot.data == null) {
      //         return LoginScreen();
      //       }

      //       return HomeScreen();
      //     }
      //     return Scaffold();
      //   },
      // ),
    );
  }
}
