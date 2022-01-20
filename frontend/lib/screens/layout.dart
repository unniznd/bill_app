import 'package:flutter/material.dart';
import 'package:frontend/provider/layout_provider.dart';
import 'package:provider/provider.dart';
import 'home.dart';
import 'account.dart';
import 'stock.dart';
import 'report.dart';
import 'bill.dart';

class LayoutScreen extends StatefulWidget {
  const LayoutScreen({Key? key}) : super(key: key);

  @override
  _LayoutScreenState createState() => _LayoutScreenState();
}

class _LayoutScreenState extends State<LayoutScreen> {
  List<Widget> screens = [
    HomeScreen(),
    StockScreen(),
    BillScreen(),
    AccountScreen(),
    ReportScreen()
  ];
  @override
  Widget build(BuildContext context) {
    double width = MediaQuery.of(context).size.width;
    double height = MediaQuery.of(context).size.height;
    var provider = Provider.of<LayoutProvider>(context);
    return Scaffold(
      body: screens[provider.selectedIndex],
      bottomNavigationBar: ChangeNotifierProvider(
        create: (context) => LayoutProvider(),
        child: BottomNavigationBar(
          backgroundColor: Colors.transparent,
          selectedItemColor: Colors.black,
          elevation: 0,
          type: BottomNavigationBarType.fixed,
          currentIndex: provider.selectedIndex,
          onTap: (index) {
            provider.setSelectedScreenIndex(index);
          },
          items: [
            BottomNavigationBarItem(
              icon: Icon(Icons.home),
              label: "Home",
            ),
            BottomNavigationBarItem(
              icon: Icon(Icons.settings),
              label: "Stock",
            ),
            BottomNavigationBarItem(
              icon: Icon(Icons.monetization_on),
              label: "Bill",
            ),
            BottomNavigationBarItem(
              icon: Icon(Icons.account_box),
              label: "Account",
            ),
            BottomNavigationBarItem(
              icon: Icon(Icons.receipt),
              label: "Report",
            )
          ],
        ),
      ),
    );
  }
}
