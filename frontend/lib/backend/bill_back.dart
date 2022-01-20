import 'dart:convert';

import 'config.dart';

Future<String> getBillnumber() async {
  var response = await getReq("sale/bill/");
  var responseJson = jsonDecode(response.body);

  return (responseJson[0]["billnumber"] + 1).toString();
}
