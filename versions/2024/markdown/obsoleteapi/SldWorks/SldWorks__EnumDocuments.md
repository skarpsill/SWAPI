---
title: "SldWorks::EnumDocuments"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__EnumDocuments.htm"
---

# SldWorks::EnumDocuments

This method is obsolete and has been superseded
by[SldWorks::EnumDocuments2](sldworksAPI.chm::/SldWorks/SldWorks__EnumDocuments2.htm).

Description

This method gets the enumerated
list of documents that are currently open in the application.

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = SldWorks->EnumDocuments(
&retval )

(Table)=========================================================

| Output: | (LPENUMDOCUMENTS) retval | Pointer to the enumerated list of documents |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

#### Remarks

The list of ModelDoc2 objects contained in the EnumDocuments2 object
contain any open ModelDoc2 pointer. This includes ModelDoc2 objects that
may have been opened as file references; for example, from an assembly
or drawing.

You may want to use the ModelDoc2::Visible property to determine if
a particular document has its own window and is visible to the user.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="SldWorks_Object$$**$$EnumDocuments_Object$$**$$ZEnumDocuments$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\SldWorks\SldWorks__EnumDocuments.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZExample_Traverse_All_Open_Documents$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\SldWorks\SldWorks__EnumDocuments.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
