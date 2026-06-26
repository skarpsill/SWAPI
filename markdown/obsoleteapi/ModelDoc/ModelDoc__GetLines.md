---
title: "ModelDoc::GetLines"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetLines.htm"
---

# ModelDoc::GetLines

This
method is obsolete and has been superseded by[ModelDoc2::GetLines](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetLines.htm).

Description

This method gets all of the lines in the current sketch.

Syntax (OLE Automation)

retval = ModelDoc.GetLines ()

(Table)=========================================================

| Return: | (VARIANT) retval | VARIANT of type SafeArray |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->IGetLines ( retval
)

(Table)=========================================================

| Output: | (double*) retval | Pointer to an array doubles |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The return value is the following array of doubles:

[LineType,
StartPtX, StartPtY, StartPtZ, EndPtX, EndPtY, EndPtZ,...
]

where this array of 7 values repeats
itself for each line in the current sketch. The number of doubles returned
will be (number of lines* 7).
To determine the number of lines in the current sketch, use[ModelDoc::GetLineCount](ModelDoc__GetLineCount.htm).

See swLineTypes_e for valid line types.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
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
<param name="Items" value="ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="" >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc\ModelDoc__GetLines.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
