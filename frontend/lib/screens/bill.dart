import 'package:flutter/material.dart';
import 'package:frontend/backend/bill_back.dart';
import 'package:frontend/model/stock_model.dart';
import 'package:provider/provider.dart';
import 'package:frontend/provider/bill_provider.dart';
import 'package:frontend/model/stock_model.dart';

class BillScreen extends StatefulWidget {
  const BillScreen({Key? key}) : super(key: key);

  @override
  _BillScreenState createState() => _BillScreenState();
}

class _BillScreenState extends State<BillScreen> {
  TextEditingController billnumber = new TextEditingController();

  Future<void> getStock() async {
    await Provider.of<BillProvider>(context, listen: false).getAllItem();
  }

  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    Future.delayed(Duration.zero, () {
      this.getStock();
    });
  }

  @override
  Widget build(BuildContext context) {
    double width = MediaQuery.of(context).size.width;
    double height = MediaQuery.of(context).size.height;
    return FutureBuilder(
      future: Future.wait([
        getBillnumber(),
      ]),
      builder: (context, AsyncSnapshot<List<dynamic>> snapshot) {
        late List itemList;
        List<String> item_code = ['Item Code'];
        late var _currentItemCode = item_code[0];
        List<String> item_name = ['Item Name'];
        List<double> item_quantity = [];
        List<double> item_price = [];

        if (snapshot.connectionState == ConnectionState.done) {
          if (snapshot.hasData) {
            billnumber.text = (snapshot.data?[0]).toString();
            print(Provider.of<BillProvider>(context).allStocks);
            return Scaffold(
              appBar: AppBar(
                backgroundColor: Colors.transparent,
                elevation: 0,
                title: Text(
                  "Make bills here!!",
                  style: TextStyle(
                    color: Colors.black,
                  ),
                ),
                actions: [
                  Icon(
                    Icons.history,
                    color: Colors.black,
                    size: 30,
                  ),
                  SizedBox(
                    width: 20,
                  ),
                  Icon(
                    Icons.shopping_cart,
                    color: Colors.black,
                    size: 30,
                  ),
                  SizedBox(
                    width: 10,
                  ),
                ],
              ),
              body: SafeArea(
                child: SingleChildScrollView(
                  child: Container(
                    margin: EdgeInsets.all(10),
                    child: Column(
                      children: [
                        TextField(
                          controller: billnumber,
                          enabled: false,
                          decoration: InputDecoration(
                            border: OutlineInputBorder(),
                            label: Text('Bill Number'),
                          ),
                        ),
                        SizedBox(
                          height: 20,
                        ),
                        ChangeNotifierProvider(
                          create: (context) => BillProvider(),
                          child: Container(
                            decoration: BoxDecoration(
                              color: Color.fromRGBO(227, 227, 227, 1),
                              borderRadius: BorderRadius.circular(10),
                            ),
                            child: DropdownButton<Stock>(
                              isExpanded: true,
                              value:
                                  Provider.of<BillProvider>(context).selected,
                              items: Provider.of<BillProvider>(context)
                                  .allStocks
                                  .map<DropdownMenuItem<Stock>>((Stock stock) {
                                return DropdownMenuItem<Stock>(
                                  value: stock,
                                  child: Text(stock.itemCode),
                                );
                              }).toList(),
                              onChanged: (final Stock? stock) {
                                Provider.of<BillProvider>(context,
                                        listen: false)
                                    .setSelectedItem(stock);
                              },
                            ),
                          ),
                        )
                      ],
                    ),
                  ),
                ),
              ),
            );
          } else {
            return Scaffold(
              body: Center(
                child: Text("Failed to load!"),
              ),
            );
          }
        }
        return Scaffold(
          body: Center(
            child: CircularProgressIndicator(),
          ),
        );
      },
    );
  }
}
