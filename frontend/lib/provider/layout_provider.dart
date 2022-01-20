import 'package:flutter/material.dart';
import 'package:frontend/screens/home.dart';
import 'package:frontend/screens/account.dart';
import 'package:frontend/screens/stock.dart';
import 'package:frontend/screens/report.dart';
import 'package:frontend/screens/bill.dart';

class LayoutProvider with ChangeNotifier {
  int _selectedScreenIndex = 2;

  int get selectedIndex => _selectedScreenIndex;

  void setSelectedScreenIndex(int index) {
    _selectedScreenIndex = index;
    notifyListeners();
  }
}
