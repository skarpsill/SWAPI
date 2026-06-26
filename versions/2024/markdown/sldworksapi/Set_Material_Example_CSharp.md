---
title: "Set Material Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Material_Example_CSharp.htm"
---

# Set Material Example (C#)

This example shows how to get the names of the material schema, material
databases, and bodies in a part document. This example also shows how
to apply a SOLIDWORKS Material to all of the bodies in a part document.

```vb
//----------------------------------------------------
 // Preconditions:
 // 1. Verify that the specified document exists.
 // 2. Open the Immediate window.
 //
 // Postconditions:
 // 1. Opens the specified part document.
 // 2. Applies the material ABS PC (polycarbonate plastic)
 //    from the SOLIDWORKS Material database to all
 //    bodies in the part.
 // 3. To verify, examine:
 //    * DisplayManager tab
 //    * graphics area
 //    * Immediate window
 //
 // NOTE: Because the part document is used elsewhere,
 // do not save changes.
 //----------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 using System.Diagnostics;
 namespace GetMaterialBodyCSharp.csproj
 {
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}public partial class SolidWorksMacro
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Main()
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDoc2 swModel = default(ModelDoc2);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}PartDoc swPart = default(PartDoc);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Body2 swBody = default(Body2);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int errors = 0;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int warnings = 0;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}object[] vMatDBarr = null;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}object[] vMatDB = null;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}object[] Bodies = null;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int BodyMaterialError = 0;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}string sMatName = "";
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}string sMatDB = "";
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int i = 0;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int j = 0;

 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Open the document
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel = (ModelDoc2)swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\multibody\\multi_inter.sldprt", (int)swDocumentTypes_e.swDocPART,
 (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swPart = (PartDoc)swModel;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Get the material schema and names
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// of available materials databases
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}vMatDBarr = (object[])swApp.GetMaterialDatabases();
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Material schema pathname = " + swApp.GetMaterialSchemaPathName());
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}for (i=0; i < vMatDBarr.Length; i++)
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" Material database: " + vMatDB);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("");
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Bodies = (object[])swPart.GetBodies2((int)swBodyType_e.swAllBodies, false);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}for (j = 0; j < Bodies.Length; j++)
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swBody = (Body2)Bodies[j];
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}// Get the name of the body
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(swBody.Name);

                 swBody.Select2(false, null);

 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}// Set the SOLIDWORKS material for that body
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}BodyMaterialError = swBody.SetMaterialProperty("Default", "solidworks
 materials.sldmat", "ABS PC");
                 // Comment out the previous statement and uncomment the following statement to use
 custom material
 kadov_tag{{<spaces>}}                //kadov_tag{{</spaces>}}BodyMaterialError = swBody.SetMaterialProperty("Default", "custom materials.sldmat",
 "Custom Plastic");

 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}// Get the names of the body's material and the
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}// database to which it belongs
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}sMatName = swBody.GetMaterialPropertyName("", out sMatDB);
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}if (string.IsNullOrEmpty(sMatName))
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print("Body " + j + "'s material name: No material applied");
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}}
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}else
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print("Body " + j + "'s material name: " + sMatName);
 kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print("Body " + j + "'s material database: " + sMatDB);
 kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" ");
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}}
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// <summary>
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// The SldWorks swApp variable is pre-assigned for you.
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// </summary>
  kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
 }
```
