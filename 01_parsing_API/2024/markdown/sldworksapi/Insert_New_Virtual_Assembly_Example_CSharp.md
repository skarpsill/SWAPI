---
title: "Insert New Virtual Assembly Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_New_Virtual_Assembly_Example_CSharp.htm"
---

# Insert New Virtual Assembly Example (C#)

This example shows how to insert an assembly as a virtual component into the
main assembly or selected sub-assembly.

//-------------------------------------------------------------------------

// Preconditions: Open
an assembly document.

//

// Postconditions: A
new virtual component displays in the

// FeatureManager design tree.

//---------------------------------------------------------------------------

using SolidWorks.Interop.sldworks;

using SolidWorks.Interop.swconst;

using System;

using System.Diagnostics;

namespace InsertNewVirtualAssembly_CSharp.csproj

{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}partial
class SolidWorksMacro

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ModelDoc2
swDoc;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}AssemblyDoc
swADoc;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Component2
swComp;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}long
status;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}public
void Main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDoc
= (ModelDoc2)swApp.ActiveDoc;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swADoc
= (AssemblyDoc)swDoc;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swComp
= null;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}status
= swADoc.InsertNewVirtualAssembly(out
swComp);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if
((swComp == null))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}System.Windows.Forms.MessageBox.Show("Virtual
component did not get created.");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}else

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("New
virtual component: " + swComp.Name2);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Is
virtual: " + swComp.IsVirtual);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}public
SldWorks swApp;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

}
