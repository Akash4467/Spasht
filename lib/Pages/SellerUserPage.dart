import 'package:flutter/material.dart';

import 'QRScannerPage.dart';
class SellerUserPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Seller Scanner")),
      body: Center(
        child: ElevatedButton(
          onPressed: () => Navigator.push(
              context, MaterialPageRoute(builder: (_) => QRScannerPage())),
          child: Text("Scan QR and Update Product Status"),
        ),
      ),
    );
  }
}