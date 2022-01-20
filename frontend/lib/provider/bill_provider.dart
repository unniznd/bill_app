import 'package:flutter/material.dart';
import 'package:frontend/backend/config.dart';
import 'dart:convert';
import 'package:frontend/model/stock_model.dart';

class BillProvider with ChangeNotifier {
  List<Stock> _stockList = [];
  List<Stock> get allStocks {
    return [..._stockList];
  }

  Stock? _selectedItem;

  Stock? get selected => _selectedItem;

  Future<void> getAllItem() async {
    var response = await getReq("stock/");
    List all_items = json.decode(response.body);
    final List<Stock> stockList = [];

    all_items.forEach((element) {
      stockList.add(Stock(element['itemCode'].toString(), element['itemName'],
          element['quantity'], element['price']));
    });
    _stockList = stockList;
    notifyListeners();
  }

  void setSelectedItem(Stock? s) {
    _selectedItem = s;
    notifyListeners();
  }
}
