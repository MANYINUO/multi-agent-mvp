#!/bin/bash
cd backend
uvicorn main:app --reload &
cd ..
cd frontend
npm install
npm start
