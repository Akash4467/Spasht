import 'package:flutter/material.dart';

import 'FarmDashboard.dart';
class FarmRegistrationPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Farm Registration")),
      body: Padding(
        padding: EdgeInsets.all(16.0),
        child: Column(
          children: [
            TextField(decoration: InputDecoration(labelText: "Farm Name")),
            TextField(decoration: InputDecoration(labelText: "Location")),
            TextField(decoration: InputDecoration(labelText: "Crops/Products")),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: () => Navigator.push(
                  context, MaterialPageRoute(builder: (_) => FarmDashboard())),
              child: Text("Register"),
            ),
          ],
        ),
      ),
    );
  }
}
