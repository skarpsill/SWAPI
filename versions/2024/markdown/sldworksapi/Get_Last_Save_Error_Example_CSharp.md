---
title: "Get Last Save Error Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Last_Save_Error_Example_CSharp.htm"
---

# Get Last Save Error Example (C#)

This example shows
how to get the last save error issued by Microsoft in the current SOLIDWORKS
session.
//------------------------------------------------------------------- // Preconditions: // 1. Open a SOLIDWORKS session and cause Microsoft to issue a save error. // 2. Open the Immediate window. // // Postconditions: // 1. Gets the last save error issued by Microsoft. // 2. Examine the Immediate window. //--------------------------------------------------------------------using SolidWorks.Interop.sldworks;

using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;

namespace Macro1CSharp.csproj

{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}partial
class SolidWorksMacro
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}object
varPath;
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}object
varError;
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}object
varMessage;
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}long
err;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}public
void Main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}varMessage
= swApp.GetLastSaveError(out varPath,
out varError);
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if
(!(varError == null))
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}err
= (long)varError;
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if
(!(err == 0))
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Document generating the save error: " + (String)varPath);
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Error code: " + (String)varError);
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Error message: " + (String)varMessage);
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}kadov_tag{{<spaces>}}
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}else
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("This
SOLIDWORKS
session has not experienced a save error.");
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}public
SldWorks swApp;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

}
