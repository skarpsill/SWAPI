---
title: "DrawingDoc::InsertCustomSymbol"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__InsertCustomSymbol.htm"
---

# DrawingDoc::InsertCustomSymbol

This method is obsolete and has been superseded by[DrawingDoc::InsertCustomSymbol2](DrawingDoc__InsertCustomSymbol2.htm).

Description

This method inserts a custom symbol into the document.

Syntax (OLE Automation)

void
DrawingDoc.InsertCustomSymbol ( symbolPath )

(Table)=========================================================

| Input: | (BSTR)
symbolPath | Filename
of the custom symbol |
| --- | --- | --- |

Syntax (COM)

status = DrawingDoc->InsertCustomSymbol
( symbolPath )

(Table)=========================================================

| Input: | (BSTR) symbolPath | Filename of the custom symbol |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method depends on a selected
item. If nothing is selected, SolidWorks takes no action and this method
returns NULL.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
style="width: 1px; height: 1px;"
width=1
height=1>
<param name=_Version value="65536" >
<param name=_ExtentX value="26" >
<param name=_ExtentY value="26" >
<param name=_StockProps value="13" >
<param name=ForeColor value="0" >
<param name=BackColor value="12632256" >
<param name=UseButton value="0" >
<param name=ControlLabel value="See Also" >
<param name=UseIcon value="0" >
<param name=Items value="DrawingDoc_Object$$**$$CustomSymbol$$**$$" >
<param name=Image value="" >
<param name=FontInfo value="MS Sans Serif,8,0,," >
<param name=_CURRENTFILEPATH value="D:\sw2003\DrawingDoc\DrawingDoc__InsertCustomSymbol.htm" >
<param name=_ID value="RelatedTopic0" >
<param name=DialogDisplay value="0" >
<param name=Frame value="" >
<param name=Window value="" >
<param name=ChmFile value="" >
<param name=DisableJump value="0" >
</object>Metadata type="DesignerControl" endspan
