# This is a basic workflow to help you get started with Actions

name: Part B

# Controls when the workflow will run
on:
  # Triggers the workflow on push or pull request events but only for the main branch
  push:
    branches: [ main ]
    paths:
      - 'a3_partb.py'
      
  pull_request:
    branches: [ main ]
    paths:
      - 'a3_partb.py'

  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

# A workflow run is made up of one or more jobs that can run sequentially or in parallel
jobs:
  # This workflow contains a single job called "build"
  build:
    # The type of runner that the job will run on
    runs-on: ubuntu-latest

    # Steps represent a sequence of tasks that will be executed as part of the job
    steps:
      # Checks-out your repository under $GITHUB_WORKSPACE, so your job can access it
      - uses: actions/checkout@v4
        with:
          path: ./assignment

      - name: Checkout Tester
        uses: actions/checkout@v4
        with:
          repository: seneca-dsa456-f23/testers
          token: ${{ secrets.TESTER_ACCESS }}
          path: ./tester

      - name: Copy python tester files
        run: cp ./tester/test_a3_partb.py ./

      - name: Copy assignment files
        run: cp ./assignment/a3_partb.py ./

      - name: Copy assignment files
        run: cp ./assignment/a3_parta.py ./

      - name: Copy assignment files
        run: cp ./assignment/a1_partc.py ./

      - name: Copy assignment files
        run: cp ./assignment/a1_partd.py ./

      # Runs a single command using the runners shell
      - name: Run tester
        run: python test_a3_partb.py


