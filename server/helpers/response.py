class ResponseHelper:
    @staticmethod
    def format_response(data, next=None, prev=None):
        response = {
            "count": len(data),
            "next": next,
            "prev": prev,
            "data": data,
        }

        return response
