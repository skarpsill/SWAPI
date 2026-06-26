---
title: "Save as De-Featured File Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Save_As_Defeatured_File_Example_CSharp.htm"
---

# Save as De-Featured File Example (C#)

This example shows how to de-feature an assembly and save it as a part.

//-----------------------------------------------------------------------------
// Preconditions:
// 1. Openpublic_documents\samples\tutorial\floxpress\ball valve\ball_valve.sldasm.
// 2. Verify that**c:\temp**exists.
//
// Postconditions:
// 1. Saves the assembly as a de-featured part.
// 2. Open**c:\temp\ball_valve.sldprt**to verify.
//------------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;

namespace SaveFileAsDeFeaturedPart_CSharp.csproj

{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}partial
class SolidWorksMacro

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ModelDoc2
swModel;
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bool
boolstatus;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}public
void Main()
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel= (ModelDoc2)swApp.**ActiveDoc**;
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= swModel.**Extension**.SaveDeFeaturedFile("C:\\temp\\ball_valve.sldprt");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}public
SldWorks swApp;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

}
