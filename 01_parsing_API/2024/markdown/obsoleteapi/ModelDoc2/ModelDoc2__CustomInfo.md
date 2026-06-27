---
title: "ModelDoc2::CustomInfo"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__CustomInfo.htm"
---

# ModelDoc2::CustomInfo

This
property is obsolete and has been superseded by[ModelDoc2::CustomInfo2](ModelDoc2__CustomInfo2.htm).

Description

This property gets and sets file custom information for the SolidWorks
document.

Syntax (OLE Automation)

Value = ModelDoc2.CustomInfo (fieldName) (VB
Get property)

ModelDoc2. CustomInfo(fieldName) =
Value (VB Set property)

Value = ModelDoc2.SetCustomInfo(fieldName) (C++
Get property)

ModelDoc2.SetCustomInfo(fieldName,
Value) (C++ Set property)

(Table)=========================================================

| Input: | (long) fieldName | Name of field |
| --- | --- | --- |
| Property: | (BSTR) value | Text in the field |

Syntax (Com)

Status = ModelDoc.get_CustomInfo(fieldName,
&Value) (C++ Get property)

Status = ModelDoc.put_CustomInfo(fieldName,
Value) (C++ Set property)

(Table)=========================================================

| Input: | (long) fieldName | Name of field |
| --- | --- | --- |
| Property: | (BSTR) value | Text in the field |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

As per Microsoft recommendations for OLE support, the file summary information
for SolidWorks documents is written as an OLE property set into a stream
named "\005Summary Information" off the root storage of the
SolidWorks document's compound file

NOTE:MFC does not currently
provide classes that manage summary information. However, the DRAWCLI
application shipped with Visual C++ does include a sample implementation,
in the form of the class CSummInfo, that you can use as an example when
implementing your own. This class is used by the document class CDrawDoc.
DRAWCLI also includes property pages for displaying and modifying summary
information.

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
<param name="Items" value="ZReleaseNotes2001Plus$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\ModelDoc2\ModelDoc2__CustomInfo.htm" >
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
<param name="Items" value="ModelDoc2_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\ModelDoc2\ModelDoc2__CustomInfo.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
