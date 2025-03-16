import 'package:flutter/material.dart';

import 'QRScannerPage.dart';
class FarmDashboard extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Farm Dashboard")),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            ElevatedButton(
              onPressed: () {},
              child: Text("Generate QR & Barcode"),
            ),
            ElevatedButton(
              onPressed: () => Navigator.push(
                  context, MaterialPageRoute(builder: (_) => QRScannerPage())),
              child: Text("Scan QR Code"),
            ),
          ],
        ),
      ),
    );
  }
}
