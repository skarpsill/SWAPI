---
title: "DimXpert Main Module Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdimxpertapi/DimXpert_Main_Module_CSharp.htm"
---

# DimXpert Main Module Example (C#)

```vb
// This module is a component of
// Get DimXpert Features and Annotations in a Model Example (C#).

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using SolidWorks.Interop.swdimxpert;
using System;
using System.Diagnostics;
using System.Collections.Generic;
using System.Collections.ObjectModel;
namespace DimXpert_text_v2_cs.csproj
{
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}partial class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//This application allows the user to view all of the DimXpert feature and annotation objects in a model.
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDoc2 swModelDoc = default(ModelDoc2);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModelDoc = (ModelDoc2)swApp.ActiveDoc;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (swModelDoc == null)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}return;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Scripting.FileSystemObject f = new Scripting.FileSystemObject();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Scripting.TextStream textStr = default(Scripting.TextStream);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}textStr = f.CreateTextFile("C:\\temp\\dimXpertInfo.txt", true, false);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (textStr == null)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Error creating temp file.");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}return;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}log("Starting DimXpert log...", textStr);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}retrieve_info_text(swApp, textStr);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}textStr.Close();
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}private void log(string text, Scripting.TextStream textStr)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(text);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}textStr.WriteLine(text);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}private void retrieve_info_text(SldWorks swapp, Scripting.TextStream textStr)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}DimXpertManager dimXpertMgr = default(DimXpertManager);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDocExtension modelDocExtension = default(ModelDocExtension);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}modelDocExtension = swapp.IActiveDoc2.Extension;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}dimXpertMgr = modelDocExtension.get_DimXpertManager(swapp.IActiveDoc2.IGetActiveConfiguration().Name,
kadov_tag{{<spaces>}}     kadov_tag{{</spaces>}}true);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}log("Model: " + swapp.IActiveDoc2.GetPathName(), textStr);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}DimXpertPart dimXpertPartObj = default(DimXpertPart);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}dimXpertPartObj = (DimXpertPart)dimXpertMgr.DimXpertPart;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SolidWorks.Interop.swdimxpert.DimXpertPart dimXpertPart = default(SolidWorks.Interop.swdimxpert.DimXpertPart);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}dimXpertPart = dimXpertPartObj;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}object[] vFeatures = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}object[] vAnnotations = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}vFeatures = (object[])dimXpertPart.GetFeatures();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}vAnnotations = (object[])dimXpertPart.GetAnnotations();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}log("------------------------", textStr);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}log("Features...", textStr);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}log("------------------------", textStr);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}DimXpertFeature featTemp = default(DimXpertFeature);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}long featureIndex = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}for (featureIndex = 0; featureIndex <= vFeatures.GetUpperBound(0); featureIndex++)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}featTemp = (DimXpertFeature)vFeatures[featureIndex];
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}DimXpertFeatureData FeatureData = new DimXpertFeatureData();
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Collection<string> featureDataText = default(Collection<string>);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}featureDataText = FeatureData.FeatureData(featTemp);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}int featureTextIndex = 0;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}log("DimXpertFeature...", textStr);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}for (featureTextIndex = 0; featureTextIndex <= featureDataText.Count - 1; featureTextIndex++)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}log(featureDataText[featureTextIndex], textStr);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}log(" ", textStr);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}log(" ", textStr);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}log("------------------------", textStr);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}log("Annotations...", textStr);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}log("------------------------", textStr);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}DimXpertAnnotation annotationTemp = default(DimXpertAnnotation);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}long annotationIndex = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}for (annotationIndex = 0; annotationIndex <= vAnnotations.GetUpperBound(0); annotationIndex++)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}annotationTemp = (DimXpertAnnotation)vAnnotations[annotationIndex];
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(annotationTemp.Name);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}DimXpertAnnotationData AnnotationData = new DimXpertAnnotationData();
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Collection<string> AnnotationDataText = default(Collection<string>);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}AnnotationDataText = AnnotationData.AnnotationData(annotationTemp, dimXpertPart);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}int annotationTextIndex = 0;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}log("DimXpertAnnotation...", textStr);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}for (annotationTextIndex = 0; annotationTextIndex <= AnnotationDataText.Count - 1; annotationTextIndex++)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}log(AnnotationDataText[annotationTextIndex], textStr);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}log(" ", textStr);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}log(" ", textStr);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}log("------------------------", textStr);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}log("Block Tolerances...", textStr);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}log("------------------------", textStr);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}listBlockTolerances_text(dimXpertPart, textStr);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}private void listBlockTolerances_text(SolidWorks.Interop.swdimxpert.DimXpertPart dimXpertPart, Scripting.TextStream textStr)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SolidWorks.Interop.swdimxpert.DimXpertBlockTolerances blockTols = default(SolidWorks.Interop.swdimxpert.DimXpertBlockTolerances);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}bool boolstatus = false;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}double lin1 = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int lin1prec = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}double lin2 = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int lin2prec = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}double lin3 = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int lin3prec = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}double ang = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SolidWorks.Interop.swdimxpert.swDimXpertISO2768PartType_e isoCode = default(SolidWorks.Interop.swdimxpert.swDimXpertISO2768PartType_e);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}blockTols = dimXpertPart.GetBlockTolerances();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if ((blockTols != null))
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}switch (blockTols.Type)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}case swDimXpertBlockToleranceType_e.swDimXpertBlockToleranceType_ASMEInch:
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}boolstatus = blockTols.GetToleranceValues(ref lin1, ref lin1prec, ref lin2, ref lin2prec, ref lin3, ref lin3prec, ref ang);
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}log("swDimXpertBlockToleranceType_ASMEInch", textStr);
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}log("Linear1: " + System.String.Format("{0:D}", lin1prec.ToString()) +
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}" Places = " + System.String.Format("{0:D}", lin1.ToString()) + " " +
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}"Linear2: " + System.String.Format("{0:D}", lin2prec.ToString()) +
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}" Places = " + System.String.Format("{0:D}", lin2.ToString()) + " " +
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}"Linear3: " + System.String.Format("{0:D}", lin3prec.ToString()) +
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}" Places = " + System.String.Format("{0:D}", lin3.ToString()) + " " +
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}"Angular = " + System.String.Format("{0:D}", (ang * 57.2957795130823).ToString()), textStr);
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}case swDimXpertBlockToleranceType_e.swDimXpertBlockToleranceType_ISO2768:
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}log("swDimXpertBlockToleranceType_ISO2768", textStr);
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}boolstatus = blockTols.GetISO2768PartType(ref isoCode);
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}switch (isoCode)
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}case swDimXpertISO2768PartType_e.swDimXpertISO2768PartType_Fine:
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}log("General Tolerance: Fine", textStr);
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}case swDimXpertISO2768PartType_e.swDimXpertISO2768PartType_Medium:
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}log("General Tolerance: Medium", textStr);
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}case swDimXpertISO2768PartType_e.swDimXpertISO2768PartType_Coarse:
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}log("General Tolerance: Coarse", textStr);
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}case swDimXpertISO2768PartType_e.swDimXpertISO2768PartType_VeryCoarse:
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}log("General Tolerance: Very Coarse", textStr);
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}       kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
}
```
