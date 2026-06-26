---
title: "Get Names of Creators of Features Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Names_of_Creators_of_Features_Examples_CPlusCPlus_COM.htm"
---

# Get Names of Creators of Features Example (C++ COM)

This example shows how to get the names of the creators of the features
in multiple part documents.

- [FeatureCreatedBy.cpp](#FeatureCreatedBy)
- [stdafx.h](#stdafx)
- [stdafx.cpp](#stdafx1)

#### FeatureCreatedBy.cpp

/*

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}PRECONDITIONS:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*
SOLIDWORKS is open and the specified input file exists in this folder:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}c:\SOLIDWORKSFilenames.txt.

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*
The SOLIDWORKS part documents listed in the input file and used by

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}this
application were installed when SOLIDWORKS was installed:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}-
C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\toolbox\braceleft.sldprt

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}-
C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\toolbox\braceright.sldprt

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}-
C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\toolbox\baseplate.sldprt

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}POSTCONDITIONS:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*
The specified output file is created in the specified folder:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}c:\SOLIDWORKSFilenamesFeatureCreators.txt.

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*
The names of the SOLIDWORKS part documents and their features

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}and
the names of the creators of those features.

*/

#include "stdafx.h"

#include <fstream> //Stream class to both read from
and write to files

#include <string>

CComBSTR makeBstr(string input);//makeBstr function prototype

using namespace std;

int _tmain()

{

ifstream infile;

ofstream outfile;

//Iniitalize COM

CoInitialize(NULL);

//Use ATL smart pointers

CComPtr<ISldWorks> swApp;

CComPtr<IModelDoc2> swModel;

CComPtr<IFeature> swFeat;

CComPtr<IFeature> swNextFeat;

long lErrors;

long lWarnings;

string sSOLIDWORKSFilename;

CComBSTR sDefaultConfiguration(L"Default");

CComBSTR sFeatureName(L"");

CComBSTR sFeatureCreator(L"");

HRESULT hres = NOERROR;

//Open input file

infile.open("C:\\SOLIDWORKSFilenames.txt",
std::ios_base::in);

//Make sure input file exists

if(!infile)

{

cout << "ERROR: Cannot open the
input file." << endl;

return 1;

}

//Open output file

outfile.open("c:\\SOLIDWORKSFilenamesFeatureCreators.txt",
std::ios_base::out );

//Make sure output file exists

if( !outfile)kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

{

cout << "ERROR: Cannot open the
output file." << endl;

infile.close();

return 1;

}

outfile << "============================================================================="
<< endl;

//Connect to currently running instance
of SOLIDWORKS

hres = swApp.CoCreateInstance(__uuidof(SldWorks),
NULL, CLSCTX_LOCAL_SERVER);

//Check results

if (S_OK != hres)

return 1;

while (!infile.eof())

{

//Read SOLIDWORKS part document name from
SOLIDWORKSFilenames.txt

getline (infile, sSOLIDWORKSFilename);

//Convert string to CComBSTR by calling
function makeBstr

CComBSTR sSWFilename = (makeBstr(sSOLIDWORKSFilename));

cout << sSOLIDWORKSFilename <<
endl;

//Open part document

hres = swApp->OpenDoc6(sSWFilename,
swDocPART, swOpenDocOptions_Silent, sDefaultConfiguration, &lErrors,
&lWarnings, &swModel);

//Check results

if (S_OK != hres || swModel == NULL)

return 1;

//Write name of SOLIDWORKS part document
in SOLIDWORKSFilenamesFeatureCreators.txt

outfile << sSOLIDWORKSFilename <<
endl;

outfile << "============================================================================="
<< endl;

//Get first feature

swModel->IFirstFeature(&swFeat);

//Iterate over features in this part document
in the FeatureManager design tree

while(swFeat)

{

//Get feature name

swFeat->get_Name(&sFeatureName);

//Get creator of feature

swFeat->get_CreatedBy(&sFeatureCreator);

//Convert feature name and creator of feature
to

//string and write to output file

CW2CT
sFeatureNameString(sFeatureName);

CW2CT
sFeatureCreatorString(sFeatureCreator);

string sFNS = _bstr_t(sFeatureNameString);

string sFCS = _bstr_t(sFeatureCreatorString);

outfile <<

"Feature "

<< sFNS <<

" created by "

<< sFCS << endl;

//Get next feature in this part document

swFeat->IGetNextFeature(&swNextFeat);

swFeat.Release();

swFeat = swNextFeat;

swNextFeat.Release();

}

outfile << "============================================================================="
<< endl;

//Close the part document

swApp->CloseDoc(sSWFilename);

swModel.Release();

swFeat.Release();

}

//Close input and output files

infile.close();

outfile.close();

swApp.Release();

//Uninitialize COM

CoUninitialize();

return 0;

}

//Function to convert string to CComBSTR

CComBSTR makeBstr(string input)

{

char* CStyleString = (char*) input.c_str();

CComBSTR retval(CStyleString);

return retval;

}

[Back to top](#Topc)

#### stdafx.h

/// stdafx.h : include file for standard system include
files,

// or project-specific include files that are used frequently,
but

// are changed infrequently

//

#pragma once

#define WIN32_LEAN_AND_MEAN // Exclude rarely-used stuff
from Windows headers

#include <stdio.h>

#include <tchar.h>

#define _ATL_CSTRING_EXPLICIT_CONSTRUCTORS // some CString
constructors will be explicit

#include <windows.h>

#include <atlbase.h>

#include <iostream>

using namespace std;kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//We
will use the standard C++ libraries for text output.

#import "sldworks.tlb" raw_interfaces_only,
raw_native_types, no_namespace, named_guidskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//the
SOLIDWORKS type library

#import "swconst.tlb"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}raw_interfaces_only,
raw_native_types, no_namespace, named_guidskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//the
SOLIDWORKS constant type library

[Back to top](#Topc)

#### stdafx.cpp

// stdafx.cpp : source file that includes just the standard
includes

// FeatureCreatedBy.pch will be the pre-compiled header

// stdafx.obj will contain the pre-compiled type information

#include "stdafx.h"

[Back to top](#Topc)
