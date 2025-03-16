import 'package:flutter/material.dart';

import 'QRScannerPage.dart';
class IndividualUserPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("QR Scanner")),
      body: Center(
        child: ElevatedButton(
          onPressed: () => Navigator.push(
              context, MaterialPageRoute(builder: (_) => QRScannerPage())),
          child: Text("Scan QR Code"),
        ),
      ),
    );
  }
}