---
title: "Create Curvature-based Mesh Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Curvature-based_Mesh_Example_CSharp.htm"
---

# Create Curvature-based Mesh Example (C#)

This example shows how to create a curvature-based mesh for a part.

```vb
 //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 //    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 // 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 //    (in the IDE, click Project > Add Reference > .NET >
 //    SolidWorks.Interop.cosworks > OK).
 // 3. Ensure that the specified part exists.
 // 4. Open the Immediate window.
 //
 // Postconditions:
 // 1. Opens the part document.
 // 2. Creates a curvature-based mesh for study, Ready.
 // 3. In SOLIDWORKS, click Ready, right-click Mesh
 //    in the Simulation study tree, and click Show Mesh.
 // 4. Gets mesh connectivity data and node normal coordinates. Because the
 //    amount of data returned is large, the display code is commented out.
 //    Uncomment the display code or add break points to inspect the returned
 //    arrays in the Locals window.
 // 5. Zoom in on the part and examine the mesh.
 // 6. Examine the Immediate window.
 //
 // NOTE: Because the part document is used elsewhere, do not save changes.
 //--------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 using System.Diagnostics;
 using SolidWorks.Interop.cosworks;
 using System.Windows.Forms;

 namespace CWMeshSWSimulationCSharp.csproj
 {
     partial class SolidWorksMacro
     {
         public void Main()
         {
             CosmosWorks COSMOSWORKS = null;
             CwAddincallback COSMOSObject =  default(CwAddincallback);
             CWModelDoc ActDoc = default(CWModelDoc);
             CWStudyManager StudyMngr =  default(CWStudyManager);
             CWStudy Study = default(CWStudy);
             CWMesh CwMesh = default(CWMesh);
             int errCode = 0;
             int errors = 0;
             int warnings = 0;
             double maxElementSize = 20.0;
             double minElementSize = 4.0;

             const string fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2017\\Simulation Examples\\bikeframe.sldprt";

             COSMOSObject = (CwAddincallback)swApp.GetAddInObject("SldWorks.Simulation");
             if (COSMOSObject == null)
                 ErrorMsg(swApp, "No Simulation add-in");
             COSMOSWORKS = (CosmosWorks)COSMOSObject.CosmosWorks;
             if (COSMOSWORKS == null)
                 ErrorMsg(swApp, "No COSMOSWORKS object");

             swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
             ActDoc = (CWModelDoc)COSMOSWORKS.ActiveDoc;
             if (ActDoc == null)
                 ErrorMsg(swApp, "No active document",  true);

             StudyMngr = (CWStudyManager)ActDoc.StudyManager;
             if (StudyMngr == null)
                 ErrorMsg(swApp, "No CWStudyManager object");
             Study = (CWStudy)StudyMngr.GetStudy(0);
             if (Study == null)
                 ErrorMsg(swApp, "No study");
             if ((Study.Name != "Ready"))
                 ErrorMsg(swApp, "Wrong study");
             Debug.Print("Name of study: " + Study.Name);

             CwMesh = (CWMesh)Study.Mesh;
             if (CwMesh == null)
                 ErrorMsg(swApp,  "No mesh");

             // Set type of mesh to curvature-based
             CwMesh.MesherType = (int)swsMesherType_e.swsMesherTypeAlternate;

             // Set mesh parameters
             CwMesh.GrowthRatio = 1.6;
             CwMesh.MinElementsInCircle = 8;
             CwMesh.GetDefaultMaxAndMinElementSize((int)swsLinearUnit_e.swsLinearUnitMillimeters, out maxElementSize, out minElementSize);

             // Create mesh
             errCode = Study.CreateMesh((int)swsLinearUnit_e.swsLinearUnitMillimeters, 20, 1);
             Debug.Print("Error code: " + errCode);
             //0 indicates successful creation of the mesh
             if (errCode != 0)
                 ErrorMsg(swApp, "Mesh failed; check error code");

             // Get maximum and minimum element sizes used for boundaries
             Debug.Print("Maximum element size used for boundaries with lowest curvature: " + CwMesh.MaxElementSize);
             Debug.Print("Minimum element size used for boundaries with highest curvature: " + CwMesh.MinElementSize);

             object[] Var1 = null;
             object[] Var = null;
             //int i = 0;
             //Debug.Print("Mesh connectivity data");
             //Debug.Print("Number of nodes in connectivity unit, node numbers in connectivity unit");
             //i = 0;
             Var = (object[])CwMesh.GetConnectivity(out errCode);
             //while (i <= Var.GetUpperBound(0))
             //{
                 //Debug.Print(Var[i].ToString());
                 //i = i + 1;
             //}

             //Debug.Print("Mesh node normals");
             //Debug.Print("Node #, x-coord, y-coord, z-coord of node's normal vector");
             //i = 0;
             Var1 = (object[])CwMesh.GetNodeOutwardDirections(out errCode);
             //while (i <= Var1.GetUpperBound(0))
             //{
                 //if (0 == i % 4)
                 //{
                     //Debug.Print("Node: " + Var1[i]);
                     //Debug.Print("  Normal vector (x, y, z coordinates):");
                // }
                 //else
                 //{
                     //Debug.Print("    " + Var1[i]);
                 //}
                 //i = i + 1;
             //}

         }

         // Error function
         public void ErrorMsg(SldWorks swApp, string Message)
         {
             MessageBox.Show(Message);
             MessageBox.Show("'*** WARNING - General");
             MessageBox.Show("'*** " + Message);
             MessageBox.Show("");

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }
 }
```
