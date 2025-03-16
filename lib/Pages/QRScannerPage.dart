import 'package:flutter/material.dart';
import 'package:mobile_scanner/mobile_scanner.dart';
import 'QRDetailsPage.dart';

class QRScannerPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Scan QR Code")),
      body: MobileScanner(
        onDetect: (capture) {
          final List<Barcode> barcodes = capture.barcodes;
          if (barcodes.isNotEmpty && barcodes.first.rawValue != null) {
            final String scannedData = barcodes.first.rawValue!;
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => QRDetailsPage(data: scannedData)),
            );
          }
        },
      ),
    );
  }
}
