import 'dart:convert';
import '../main.dart';
import 'package:http/http.dart' as http;

String BASE_URL = 'http://10.0.2.2:8000/';

headerReq() async {
  var v = {
    "Authorization": "Token " + (await storage.read(key: "token")).toString(),
    "Content-Type": "application/json"
  };
  return v;
}

postReq(String path, var body) async {
  return await http.post(
    Uri.parse(BASE_URL + path),
    headers: await headerReq(),
    body: body,
  );
}

getReq(String path) async {
  return await http.get(
    Uri.parse(BASE_URL + path),
    headers: await headerReq(),
  );
}

patchReq(String path, var body) async {
  return await http.patch(
    Uri.parse(BASE_URL + path),
    headers: await headerReq(),
    body: body,
  );
}

deleteReq(String path, var body) async {
  return await http.delete(
    Uri.parse(BASE_URL + path),
    headers: await headerReq(),
    body: body,
  );
}
