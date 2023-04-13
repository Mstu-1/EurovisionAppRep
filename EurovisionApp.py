{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "ce61ff7f-eabf-4de7-9637-5090cf1ee97e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
      "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import psycopg2\n",
    "from flask import Flask, request, jsonify\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "DATABASE_URL = \"postgres://pfvtqhat:14XksV2ktbWNGWeEMD8bVLlEPubQ-XU0@trumpet.db.elephantsql.com/pfvtqhat\"\n",
    "\n",
    "@app.route('/insert_name', methods=['POST'])\n",
    "def insert_name():\n",
    "    name = request.form['name']\n",
    "    \n",
    "    conn = psycopg2.connect(DATABASE_URL, sslmode='require')\n",
    "    cursor = conn.cursor()\n",
    "    cursor.execute('INSERT INTO Players (Name) VALUES (%s)', (name,))\n",
    "    conn.commit()\n",
    "    cursor.close()\n",
    "    conn.close()\n",
    "    \n",
    "    return jsonify({'status': 'success'})\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(port=8080)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
