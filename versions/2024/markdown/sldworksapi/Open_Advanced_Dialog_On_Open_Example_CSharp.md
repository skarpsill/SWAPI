---
title: "Open Advanced Dialog on Document Open Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Open_Advanced_Dialog_On_Open_Example_CSharp.htm"
---

# Open Advanced Dialog on Document Open Example (C#)

This example shows how to display an advanced dialog box before opening a
document.

//----------------------------------------------------------------------
// Preconditions: Verify that the specified model document to open exists.
//
// Postconditions:
//kadov_tag{{<spaces>}}1.
Displays the Configure Document dialog box before the model
// document opens.
//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}2.
Click**OK**to close the dialog box.
//kadov_tag{{<spaces>}}3.
Close the document without saving.
//---------------------------------------------------------------------------

using SolidWorks.Interop.sldworks;

using SolidWorks.Interop.swconst;

using System;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}partial
class SolidWorksMacro

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}public
void Main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ModelDoc2
myDoc = default(ModelDoc2);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}DocumentSpecification
openDocParams = default(DocumentSpecification);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}openDocParams
= (DocumentSpecification)swApp.**GetOpenDocSpec**("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\motionstudies\\valve_cam.sldasm");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}openDocParams.DocumentType
= (int)swDocumentTypes_e.swDocASSEMBLY;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}openDocParams.InteractiveAdvancedOpen= true;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}myDoc
= swApp.**OpenDoc7**(openDocParams);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}public
SldWorks swApp;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}
