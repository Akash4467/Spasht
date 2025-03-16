import 'package:flutter/material.dart';

import 'FarmRegistrationPage.dart';
import 'IndividualUserPage.dart';
import 'SellerUserPage.dart';
class LoginPage extends StatelessWidget {
  final String userType;
  LoginPage({required this.userType});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("$userType Login")),
      body: Padding(
        padding: EdgeInsets.all(16.0),
        child: Column(
          children: [
            TextField(decoration: InputDecoration(labelText: "Username")),
            TextField(decoration: InputDecoration(labelText: "Password"), obscureText: true),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                if (userType == "Farm") {
                  Navigator.push(context, MaterialPageRoute(builder: (_) => FarmRegistrationPage()));
                } else if (userType == "Seller") {
                  Navigator.push(context, MaterialPageRoute(builder: (_) => SellerUserPage()));
                } else {
                  Navigator.push(context, MaterialPageRoute(builder: (_) => IndividualUserPage()));
                }
              },
              child: Text("Login"),
            ),
          ],
        ),
      ),
    );
  }
}