import 'package:flutter/material.dart';
import 'package:frontend/backend/bill_back.dart';
import 'package:frontend/provider/bill_provider.dart';
import 'package:frontend/provider/layout_provider.dart';
import 'package:frontend/screens/bill.dart';
import 'package:frontend/screens/layout.dart';
import 'package:provider/provider.dart';
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
    return MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (_) => BillProvider()),
        ChangeNotifierProvider(create: (_) => LayoutProvider())
      ],
      child: MaterialApp(
        debugShowCheckedModeBanner: false,
        theme: ThemeData(
          scaffoldBackgroundColor: Colors.white,
        ),
        // home: LayoutScreen(),
        home: FutureBuilder(
          future: storage.read(key: "token"),
          builder: (context, snapshot) {
            if (snapshot.connectionState == ConnectionState.done) {
              if (snapshot.data == null) {
                return LoginScreen();
              }

              return LayoutScreen();
            }
            return Scaffold();
          },
        ),
      ),
    );
  }
}
