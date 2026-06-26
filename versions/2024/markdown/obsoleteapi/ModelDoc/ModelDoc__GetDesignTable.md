---
title: "ModelDoc::GetDesignTable"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetDesignTable.htm"
---

# ModelDoc::GetDesignTable

This
method is obsolete and has been superseded by[ModelDoc2::GetDesignTable](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetDesignTable.htm).

Description

This method returns the DesignTable object
associated with this part or assembly document.

Syntax (OLE Automation)

retval = ModelDoc.GetDesignTable ( )

(Table)=========================================================

| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the DesignTable
object |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->IGetDesignTable ( &retval
)

(Table)=========================================================

| Output: | (LPDESIGNTABLE) retval | Pointer to the DesignTable object |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If this method called from a drawing document,
NULL ise returned. To access design tables from a drawing document you
must get the ModelDoc object associated with a particular drawing view,
and then call this method from that ModelDoc object. To determine if a
drawing view has a design table associated with it, use View::HasDesignTable.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$ZGetDesignTable$$**$$DesignTable_Object$$**$$View::HasDesignTable$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__GetDesignTable.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
