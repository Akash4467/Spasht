from fastapi import FastAPI, HTTPException, Depends, Header
from web3 import Web3
import firebase_admin
from firebase_admin import credentials, auth
import os
from dotenv import load_dotenv

# Load private key securely
load_dotenv()
PRIVATE_KEY = os.getenv("PRIVATE_KEY")

# Polygon RPC & Contract details
RPC_URL = "https://icy-indulgent-resonance.matic-amoy.quiknode.pro/1d85a5b1735227b08366a6cc36047b36f302fb13"  # Replace this
CONTRACT_ADDRESS = "0xED1160F9A5366c67db19D47b9f0C303255c21d94"  # Replace this

# Load Firebase credentials
cred = credentials.Certificate("firebase_credentials.json")  # Replace with your Firebase key
firebase_admin.initialize_app(cred)

# Connect to Web3
w3 = Web3(Web3.HTTPProvider(RPC_URL))
account = w3.eth.account.from_key(PRIVATE_KEY)

# Load Smart Contract ABI (Add your full contract ABI here)
ABI = [[
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "uint256",
				"name": "qrId",
				"type": "uint256"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "farmer",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "farmLocation",
				"type": "string"
			}
		],
		"name": "QRRegistered",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "uint256",
				"name": "qrId",
				"type": "uint256"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "buyer",
				"type": "address"
			}
		],
		"name": "QRScanned",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "uint256",
				"name": "qrId",
				"type": "uint256"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "seller",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "location",
				"type": "string"
			}
		],
		"name": "QRUpdated",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "user",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "enum Spasht.UserType",
				"name": "userType",
				"type": "uint8"
			}
		],
		"name": "UserRegistered",
		"type": "event"
	},
	{
		"inputs": [],
		"name": "qrCounter",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "qrs",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			},
			{
				"internalType": "address",
				"name": "farmer",
				"type": "address"
			},
			{
				"internalType": "string",
				"name": "farmLocation",
				"type": "string"
			},
			{
				"internalType": "bool",
				"name": "exists",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_farmLocation",
				"type": "string"
			}
		],
		"name": "registerQR",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_name",
				"type": "string"
			},
			{
				"internalType": "enum Spasht.UserType",
				"name": "_userType",
				"type": "uint8"
			}
		],
		"name": "registerUser",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_qrId",
				"type": "uint256"
			}
		],
		"name": "scanQR",
		"outputs": [
			{
				"components": [
					{
						"internalType": "uint256",
						"name": "id",
						"type": "uint256"
					},
					{
						"internalType": "address",
						"name": "farmer",
						"type": "address"
					},
					{
						"internalType": "string",
						"name": "farmLocation",
						"type": "string"
					},
					{
						"internalType": "string[]",
						"name": "journey",
						"type": "string[]"
					},
					{
						"internalType": "bool",
						"name": "exists",
						"type": "bool"
					}
				],
				"internalType": "struct Spasht.QR",
				"name": "",
				"type": "tuple"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_qrId",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "_location",
				"type": "string"
			}
		],
		"name": "updateQR",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "users",
		"outputs": [
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"internalType": "enum Spasht.UserType",
				"name": "userType",
				"type": "uint8"
			},
			{
				"internalType": "bool",
				"name": "registered",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]]  # Add full ABI here
contract = w3.eth.contract(address=Web3.to_checksum_address(CONTRACT_ADDRESS), abi=ABI)

app = FastAPI()

# 🔹 Helper function to verify Firebase ID Token
def verify_firebase_token(token: str = Header(...)):
    try:
        decoded_token = auth.verify_id_token(token)
        return decoded_token  # Returns user details
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid Firebase Token")

# 🔹 Helper function to send blockchain transactions
def send_transaction(func, *args):
    txn = func(*args).build_transaction({
        "from": account.address,
        "gas": 2000000,
        "nonce": w3.eth.get_transaction_count(account.address),
    })
    signed_txn = w3.eth.account.sign_transaction(txn, PRIVATE_KEY)
    txn_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    return txn_hash.hex()

# 🔹 Register QR (Only for Farmers, fetch user from Firebase)
@app.post("/registerQR")
async def register_qr(farm_location: str, user_data=Depends(verify_firebase_token)):
    try:
        user_name = user_data.get("name", "Unknown")  # Get name from Firebase
        user_uid = user_data.get("uid")  # Get Firebase user ID
        print(f"Registering QR for {user_name} (UID: {user_uid}) at {farm_location}")

        txn_hash = send_transaction(contract.functions.registerQR, farm_location)
        return {"status": "success", "txHash": txn_hash, "user": user_name, "location": farm_location}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 🔹 Update QR (Only for Sellers/Farmers, fetch user from Firebase)
@app.post("/updateQR")
async def update_qr(qr_id: int, location: str, user_data=Depends(verify_firebase_token)):
    try:
        user_name = user_data.get("name", "Unknown")
        user_uid = user_data.get("uid")
        print(f"Updating QR {qr_id} by {user_name} (UID: {user_uid}) at {location}")

        txn_hash = send_transaction(contract.functions.updateQR, qr_id, location)
        return {"status": "success", "txHash": txn_hash, "updated_by": user_name, "new_location": location}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 🔹 Scan QR (Retrieve Product History & Fetch Firebase User)
@app.get("/scanQR/{qr_id}")
async def scan_qr(qr_id: int, user_data=Depends(verify_firebase_token)):
    try:
        user_name = user_data.get("name", "Unknown")
        user_uid = user_data.get("uid")

        qr_data = contract.functions.scanQR(qr_id).call()
        if not qr_data[4]:  # Check if QR exists
            raise HTTPException(status_code=404, detail="QR not found")

        print(f"QR {qr_id} scanned by {user_name} (UID: {user_uid})")

        return {
            "id": qr_data[0],
            "farmer": qr_data[1],
            "farmLocation": qr_data[2],
            "journey": qr_data[3],
            "exists": qr_data[4],
            "scanned_by": user_name
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
