from fastapi import FastAPI

app = FastAPI(title='WorkoutApi')

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(
        'main:app',
        host='localhost',
        port=5000,
        log_level='info',
        reload=True)
