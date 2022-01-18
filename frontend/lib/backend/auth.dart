import './config.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import '../main.dart';

Future<bool> authenticate(String username, var password) async {
  var response = await http.post(
    Uri.parse(BASE_URL + 'login/'),
    body: {"username": username, "password": password.toString()},
  );

  if (response.statusCode == 200) {
    final Map auth = json.decode(response.body);

    await storage.write(key: "token", value: auth['token']);
    return true;
  }
  return false;
}
