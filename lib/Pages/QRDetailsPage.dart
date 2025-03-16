import 'package:flutter/material.dart';
class QRDetailsPage extends StatelessWidget {
  final String data;
  QRDetailsPage({required this.data});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("QR Details")),
      body: Padding(
        padding: EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text("QR Code Data: $data", style: TextStyle(fontSize: 18)),
            SizedBox(height: 10),
            Text("Status Updates:", style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold)),
          ],
        ),
      ),
    );
  }
}