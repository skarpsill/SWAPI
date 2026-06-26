---
title: "ModelDocExtension::PrintOut"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDocExtension/ModelDocExtension__PrintOut.htm"
---

# ModelDocExtension::PrintOut

This method is obsolete and has been superseded
by[ModelDocExtension::PrintOut2](sldworksAPI.chm::/ModelDocExtension/ModelDocExtension__PrintOut2.htm).

Description

This method prints the document with options
and without any dialogs or message boxes

Syntax (OLE Automation)

void ModelDocExtension.PrintOut ( FromPage, ToPage,
Copies, Collate, Printer, PrintFileName )

(Table)=========================================================

| Input: | (long) FromPage | First page in the range of pages to print |
| --- | --- | --- |
| Input: | (long) ToPage | Last page in the range of pages to print |
| Input: | (long) Copies | Number of copies to print |
| Input: | (VARIANT_BOOL) Collate | TRUE collates the copies, FALSE does not |
| Input: | (BSTR) Printer | Name of the printer queue; if you pass a NULL string, then this method
prints to the current SolidWorks printer; you can use ModelDoc2::Printer
to set the current SolidWorks printer |
| Input: | (BSTR) PrintFileName | Name of the file to print to |

Syntax (COM)

status = ModelDocExtension->PrintOut ( FromPage,
ToPage, Copies, Collate, Printer, PrintFileName )

Parameters Table Start

(Table)=========================================================

| Input: | (long) FromPage | First page in the range of pages to print |
| --- | --- | --- |
| Input: | (long) ToPage | Last page in the range of pages to print |
| Input: | (long) Copies | Number of copies to print |
| Input: | (VARIANT_BOOL) Collate | TRUE collates the copies, FALSE does not |
| Input: | (BSTR) Printer | Name of the printer queue; if you pass a NULL string, then this method
prints to the current SolidWorks printer; you can use ModelDoc2::Printer
to set the current SolidWorks printer |
| Input: | (BSTR) PrintFileName | Name of the file to print to |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method supports printing
parts, assemblies, and both single and multisheet drawings. No dialogs
or message boxes are displayed.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes2003$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDocExtension\ModelDocExtension__PrintOut.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDocExtension_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDocExtension\ModelDocExtension__PrintOut.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
