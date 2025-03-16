import 'package:flutter/material.dart';

import 'LoginPage.dart';
class UserSelectionPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Select User Type")),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            ElevatedButton(
              onPressed: () => Navigator.push(
                  context, MaterialPageRoute(builder: (_) => LoginPage(userType: "Individual"))),
              child: Text("Individual User"),
            ),
            ElevatedButton(
              onPressed: () => Navigator.push(
                  context, MaterialPageRoute(builder: (_) => LoginPage(userType: "Seller"))),
              child: Text("Seller User"),
            ),
            ElevatedButton(
              onPressed: () => Navigator.push(
                    context, MaterialPageRoute(builder: (_) => LoginPage(userType: "Farm"))),
              child: Text("Farm User"),
            ),
          ],
        ),
      ),
    );
  }
}

    