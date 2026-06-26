---
title: "Measure Selected Entities Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Measure_Selected_Entities_Example_CSharp.htm"
---

# Measure Selected Entities Example (C#)

This example shows how to use the measure tool.

```
//-----------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified part document exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified part document as read only.
// 2. Selects two faces and measures them.
// 3. Examine the Immediate window.
//-----------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace MeasureCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            Measure swMeasure = default(Measure);
            bool status = false;
            int errors = 0;
            int warnings = 0;
            string fileName = null;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\dimxpert\\coupling_auto_geo.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_ReadOnly, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("", "FACE", -0.00382117299216134, -0.0032246917626253, -0.00153854043344381, false, 0, null, 0);
            status = swModelDocExt.SelectByID2("", "FACE", 0.00547600669648318, 0.00252191841298099, 0.0050000000000523, true, 0, null, 0);
            swMeasure = (Measure)swModelDocExt.CreateMeasure();
            //Can set this to 0
            // 0 = center to center
            // 1 = minimum distance
            // 2 = maximum distance
            swMeasure.ArcOption = 0;

            status = swMeasure.Calculate(null);
            if ((status))
            {
                if ((!(swMeasure.Length == -1)))
                {
                    Debug.Print("Length: " + swMeasure.Length);
                }
                if ((!(swMeasure.Area == -1)))
                {
                    Debug.Print("Area: " + swMeasure.Area);
                }
                if ((!(swMeasure.ArcLength == -1)))
                {
                    Debug.Print("Arc length: " + swMeasure.ArcLength);
                }
                if ((!(swMeasure.ChordLength == -1)))
                {
                    Debug.Print("Chord length: " + swMeasure.ChordLength);
                }
                if ((!(swMeasure.Diameter == -1)))
                {
                    Debug.Print("Diameter: " + swMeasure.Diameter);
                }
                if ((!(swMeasure.Radius == -1)))
                {
                    Debug.Print("Radius: " + swMeasure.Radius);
                }
                if ((!(swMeasure.Perimeter == -1)))
                {
                    Debug.Print("Perimeter: " + swMeasure.Perimeter);
                }
                if ((!(swMeasure.X == -1)))
                {
                    Debug.Print("X coordinate: " + swMeasure.X);
                }
                if ((!(swMeasure.Y == -1)))
                {
                    Debug.Print("Y coordinate: " + swMeasure.Y);
                }
                if ((!(swMeasure.Z == -1)))
                {
                    Debug.Print("Z coordinate: " + swMeasure.Z);
                }
                if ((!(swMeasure.DeltaX == -1)))
                {
                    Debug.Print("DeltaX: " + swMeasure.DeltaX);
                }
                if ((!(swMeasure.DeltaY == -1)))
                {
                    Debug.Print("DeltaY: " + swMeasure.DeltaY);
                }
                if ((!(swMeasure.DeltaZ == -1)))
                {
                    Debug.Print("DeltaZ: " + swMeasure.DeltaZ);
                }
                if ((!(swMeasure.Angle == -1)))
                {
                    Debug.Print("Angle: " + swMeasure.Angle);
                }
                if ((!(swMeasure.CenterDistance == -1)))
                {
                    Debug.Print("Center distance: " + swMeasure.CenterDistance);
                }
                if ((!(swMeasure.NormalDistance == -1)))
                {
                    Debug.Print("Normal distance: " + swMeasure.NormalDistance);
                }
                if ((!(swMeasure.Distance == -1)))
                {
                    Debug.Print("Distance: " + swMeasure.Distance);
                }
                if ((!(swMeasure.TotalLength == -1)))
                {
                    Debug.Print("Total length: " + swMeasure.TotalLength);
                }
                if ((!(swMeasure.TotalArea == -1)))
                {
                    Debug.Print("Total area: " + swMeasure.TotalArea);
                }
                if ((swMeasure.IsParallel))
                {
                    Debug.Print("Is parallel: " + swMeasure.IsParallel);
                }
                if ((swMeasure.IsIntersect))
                {
                    Debug.Print("Is intersect: " + swMeasure.IsIntersect);
                }
                if ((swMeasure.IsPerpendicular))
                {
                    Debug.Print("Is perpendicular: " + swMeasure.IsPerpendicular);
                }
                if ((!(swMeasure.Projection == -1)))
                {
                    Debug.Print("Projection: " + swMeasure.Projection);
                }
                if ((!(swMeasure.Normal == -1)))
                {
                    Debug.Print("Normal: " + swMeasure.Normal);
                }
                if ((!(swMeasure.SpericalCenterDistance == -1)))
                {
                    Debug.Print("Spherical center distance: " + swMeasure.SpericalCenterDistance);
                }
                if ((swMeasure.IsConcentricSpheres))
                {
                    Debug.Print("Are concentric spheres: " + swMeasure.IsConcentricSpheres);
                }
            }
            else
            {
                Debug.Print("Invalid combination of selected entities.");
            }
            swModel.ClearSelection2(true);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
